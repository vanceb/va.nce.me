Title: Hosting my static website on AWS S3
Tags: publishing, pelican, aws, s3, route53
Summary: Publishing the Pelican site on AWS S3

I will be mainly following this [AWS HOWTO](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) guide.  This post is not intended to be a full tutorial as there are plenty of great resources already, this is meant to remind me of the process and point to the existing guides.

## Setting up an S3 bucket to host the website

Log in to your AWS account and [set up a bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html).  Because I will be using my own domain for the site I will also need to refer to [this guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)

I am using AWS Identity and Access Management (IAM) on my account so I need to setup a new user who only has access rights to this bucket. [This guide](http://blog.willj.net/2014/04/18/aws-iam-policy-for-allowing-s3cmd-to-sync-to-an-s3-bucket/) should help.  Beware the many older guides that don't include `s3:putObjectAcl` permission. The policy I applied to the user is:

``` json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:ListAllMyBuckets"
      ],
      "Resource": "arn:aws:s3:::*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::va.nce.me"]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl",
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": ["arn:aws:s3:::va.nce.me/*"]
    }
  ]
}
```

Keep hold of the credentials for the newly created user, you will need them to configure s3cmd for the upload.  You will also need to keep hold of the Static website hosting endpoint `va.nce.me.s3-website-us-east-1.amazonaws.com` in my case.

## Configure Pelican to upload site to S3 bucket

Pelican includes a build tartget in the makefile to upload to an S3 bucket.  It uses `s3cmd`, which needs to be installed and configured:

``` shell
workon pelican
pip install s3cmd
s3cmd --configure
```

If you didn't setup the bucket name when you configured pelican then you need to edit the `Makefile` and amend the `S3_BUCKET` variable.  Once you have done this you can upload the website to S3:

``` shell
make s3_upload
```

## Transferring DNS to AWS Route 53

In order to serve the website from the root of your domain from S3 you must use AWS Route 53 as your DNS provider.  I find Route 53 to be cheap, especially for low volume websites.  I followed [this guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html#Step_CreateHostedZone) to setup the hosted zone.  The name servers that will host my DNS records from Route 53 are as follows:

```
ns-336.awsdns-42.com.
ns-1509.awsdns-60.org.
ns-817.awsdns-38.net.
ns-1567.awsdns-03.co.uk.
```

My domain is currently held with [LCN](https://www.lcn.com/), so I logged into their management console to gather the details I needed to transfer to Route 53.  Key entries include:

```
A Record:

CNAME Records:
    va.nce.me
MX Records:
    aspmx.l.google.com, priority 10
    alt1.aspmx.l.google.com, priority 20
    alt2.aspmx.l.google.com, priority 20
    aspmx2.googlemail.com, priority 30
    aspmx3.googlemail.com, priority 30
TXT Records:
    google-site-verification=fdsMOUx8Go13diEXbPdLUkKOzG-REwOjqcMLF267m4o
    v=spf1 include:_spf.google.com ~all
```

Once these entries were configured in Route 53 I can change the Nameservers entry against the domain in the LCN settings to point to the Route 53 Name servers we identified above when setting up the hosted zone.

As you are now reading this on [http://va.nce.me](http://va.nce.me) it must have been successful :-)
