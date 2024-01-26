# Min/Max Waveform Analysis
This Repository gives a brief idea of how analysis endpoints for the OmniProject shall work.
The Min/Max application is designed for performing basic analysis on waveforms. 
It offers endpoints to calculate the global minimum and maximum of a set of data points and provides version information and a debug endpoint.

In order to understand how this repository creates executable releases, inspect [the repository this is forked from](https://github.com/skunkforce/fastapi-exe-tutorial/tree/master)!

## Running the Application
Once you downloaded a release and ran it from your commandline, the API will be available on `http://127.0.0.1:8484`.

## API Endpoints
1. Calculate Minimum (`/min/`)
This endpoint calculates the global minimum value from a given set of y-values in a waveform.

Usage:
To use this endpoint, send a `GET` request with a `JSON` body containing x and y lists.

Example with `curl`:

```
curl -X 'POST' 'http://127.0.0.1:8484/min/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"x": [0.1, 0.2, 0.3, 0.4], "y": [1.0, 3.5, -2.5, 4.0]}'
```

2. Calculate Maximum (`/max/`)
This endpoint calculates the global maximum value from a given set of y-values in a waveform.

Usage:
Similar to the `/min/` endpoint, send a `GET` request with `JSON` data.

Example with `curl`:

```
curl -X 'POST' 'http://127.0.0.1:8484/max/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"x": [0.1, 0.2, 0.3, 0.4], "y": [1.0, 3.5, -2.5, 4.0]}'
```

3. Version Information (`/version`)
Provides version information of the application including the app version, commit hash, build date, and maintainer.

Usage:
Send a `GET` request to the endpoint:

```
curl -X 'GET' 'http://127.0.0.1:8484/version'
```

4. Debug - Convert to Text (`/to_txt/`)
A debug endpoint that returns the request in a text format. Useful for debugging.

Usage:
Send a `POST` request with any `JSON` data:

```
curl -X 'POST' 'http://127.0.0.1:8484/to_txt/' \
-H 'Content-Type: application/json' \
-d '{"sample_key": "sample_value"}'
```

## Notes
Ensure that lists x and y in the JSON payloads for `/min/` and `/max/` have the same length.
This application is designed for demonstration purposes and might require modifications for production use.
