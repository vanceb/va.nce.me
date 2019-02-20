Title: Creating a custom node red light control
Modified: 2018-11-03 15:00
Tags: mqtt, node red, 
Summary: Creating a custom node-red light control to work with switching, movement and sunrise/sunset.

# Creating a custom node red light control

## Specification

I wanted to manage a light with a movement detector:

* Using the "on" switch should always turn on the light
* When the switch is "off" it works in automatic mode
    - If it is dark and movement is detected it will come on
    - Once movement has stopped the light should stay on for a period of time

## First attempt using the node red "function" block

Switch and movement inputs come from mqtt.  The sun input used the standard node red sunrise/sunset block and we are connected to the "every minute" output, just to make sure the block fires every minute.

~~~ javascript
msg2 = {};
msg2.topic = "light";
msg2.payload = null;

switch (msg.topic) {
    case "switch":
        msg2.payload = msg.payload;
        context.set("offtime", null);
        if (msg.payload === true) {
            context.set("mode", "manual");
        } else {
            context.set("mode", "auto");
        }
        break;
    case "movement":
        context.set("movement", msg.payload);
        if (context.get("mode") === "auto") {
            if (msg.payload === true) {
                if (context.get("dark")) {
                    msg2.payload = true;
                    context.set("offtime", null);
                }
            } else {
                // Movement stopped, so set offtime
                var offtime = new Date();
                offtime.setSeconds(offtime.getSeconds() + 5);
                context.set("offtime", offtime);
            }
        }
        break;
    case "sun":
        context.set("dark", !msg.payload);
        // Check if we should turn off the light (timed)
        if (context.get("offtime") !== null) {
            if (new Date() > context.get("offtime")) {
                // time to turn off
                msg2.payload = false;
            }
        }  
        break;
}


// Should we return the message?
if (msg2.payload === null) {
    return null;
} else {
    if (msg2.payload) {
        node.status({fill:"red",shape:"ring",text:"on"})
    } else {
        node.status({});
    }
    return msg2;
}
~~~