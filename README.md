# Haystax Twitter API Frontend

### Prerequisites

* Docker (Community Edition)
* Python 3.6.X
* `pip` 9.X.X
* Creation of a Twitter application, and the credentials that accompany it

### Overview

This application allows the user to search usernames and topics on twitter, through the use of the Twitter Search API wrapped in the TwitterAPI Python package. The tweets resulting from a search are displayed in tabular format, with the following information:
* Date of the tweet
* Content of the tweet (and a link for the full tweet, if truncated)
* Number of words in the tweet that exist in the English dictionary (`en_US`)

### Usage

To run the installation/setup for this application, and to further use this application, simply navigate to this directory and run the `run.sh` script that has been created to both build and run the docker container, simply by doing:

`$ ./run.sh`

Make sure to configure your authorization credentials in the accompanying `config.json` file, so that the Twitter Search API can authenticate on your behalf.
