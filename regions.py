#!/usr/bin/env python3

regions = {
    "US East (N. Virginia)": "us-east-1",
    "EU (Ireland)": "eu-west-1",
    "US West (N. California)": "us-west-1",
    "Asia Pacific (Singapore)": "ap-southeast-1",
    "Asia Pacific (Tokyo)": "ap-northeast-1",
    "US West (Oregon)": "us-west-2",
    "South America (São Paulo)": "sa-east-1",
    "Asia Pacific (Sydney)": "ap-southeast-2",
    "EU (Frankfurt)": "eu-central-1",
    "Asia Pacific (Seoul)": "ap-northeast-2",
    "Asia Pacific (Osaka-Local)": "ap-northeast-3",
    "Asia Pacific (Mumbai)": "ap-south-1",
    "US East (Ohio)": "us-east-2",
    "EU (London)": "eu-west-2",
    "Canada (Central)": "ca-central-1",
    "EU (Paris)": "eu-west-3",
    "EU (Stockholm)": "eu-north-1",
}


regions_list = [regions[k] for k in regions]
