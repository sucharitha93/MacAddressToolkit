# MacAddressToolkit
Validating the given Mac Address and returning the Manufacturer's Details from the input.

## Installation

Assuming that an existing docker installation is present on the host system, Use the following command to pull the docker file.

```bash
docker pull sucvenka/macaddresstoolkit:latest
```

## How to run ?

The docker run command should be supplied with an argument which is the MAC Address we intend to validate.
```bash
docker run sucvenka/macaddresstoolkit <MAC Address>
```

## How it works ?

#### Step 1: The input argument which is a MAC address is validated for the correct syntax using regular expressions.

#### Step 2: A GET request is made to "https://api.macaddress.io/v1" with api-key, output and mac address as parameters.

#### Step 3: The response is received and verified against the status code.

#### Step 4: If the status code is OK/200 then we proceed to analyse the response json object and get the manufacturer's details along with the other important details to return back to the user.

#### Step 5: If the status code is among the erroneous codes, the corresponding error is displayed back to the user.

## Sample Run

Pulling the container from docker hub
```bash
>docker pull sucvenka/macaddresstoolkit
Using default tag: latest
latest: Pulling from sucvenka/macaddresstoolkit
e4c3d3e4f7b0: Already exists
101c41d0463b: Already exists
8275efcd805f: Already exists
751620502a7a: Already exists
0a5e725150a2: Already exists
397dba5694db: Already exists
b1d09d0eabcb: Already exists
475299e7c7f3: Already exists
f7f508209c90: Already exists
80b03a2461e1: Pull complete
5c0441098293: Pull complete
d9a0d0809c98: Pull complete
36bebafaa0d0: Pull complete
Digest: sha256:eef68daf1056b66bddbc11d983a428cfba035bff0ebe4395819a8a1d185ea31c
Status: Downloaded newer image for sucvenka/macaddresstoolkit:latest
docker.io/sucvenka/macaddresstoolkit:latest
```
Checking that the container image is downloaded successfully.
```bash
>docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
sucvenka/macaddresstoolkit             latest              a80e21051f81        8 minutes ago       894MB
```
Running the container with the MAC Address as Argument

#### Case 1: Giving a valid input argument
```bash
>docker run sucvenka/macaddresstoolkit 00-15-5D-E4-54-1F
Mac address syntax validation SUCCESSFULL.

Manufacturer's Details

Name: Microsoft Corp
Address: One Microsoft Way Redmond WA 98052-8300 US
OUI: 00155D

MAC Address Details

Is Valid: True
Is virtualMachine: Hyper-V
Applications: []
Creation Date: 2005-08-04
Last Updated: 2015-09-27
```
#### Case 2: Giving an invalid input argument
```bash
>docker run sucvenka/macaddresstoolkit 00-15-5D-E4-54-1H
Invalid Mac Address
```

## Security implementations

The macaddress.io API is used in the GET requests from the python script. 
There are 2 types of Authentication Supported by this API.
##### [1] Query Based -> takes API key along with the query parameters
##### [2] Header Based -> takes API key in the header
The current implementation uses Query Based authentication.
Using APIs can expose to the threat of receiving too many query requests. This is implicitly handled using by setting a cap of 1000 on the number of requests that can be used per day. Any more requests will get the response with status code 429.

## What is not yet there in the code ?

This python script does not have a web based GUI implementation within the docker container. The API is accessed using the requests library within the python script. It can be made interactive for the user to select which details he/she would like to get for the corresponsing MAC Address.
