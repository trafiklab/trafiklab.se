---
title: Conditional GET requests
---

Conditional requests are a part of the HTTP specification. They define a condition, determining when the server should
send a response. They can define the condition that the resource must have been modified since a given timestamp
(if-modified-since) or that the resource should not match with a given checksum (if-none-match). If the client has
the latest, actual data, the if-none-match or if-modified-since validation will fail, and a 304 response is sent,
telling the client there is no new data is available. If new data is available, a 200 response is sent, including the
new data.

## If-none-match

The `If-None-Match` HTTP request header makes the request conditional.
For [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
and [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) methods, the server will send back the
requested resource, with a [`200`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) status, only if it
doesn't have an [`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) matching the given ones. For
other methods, the request will be processed only if the eventually existing
resource's [`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) doesn't match any of the values
listed.

When the condition fails (when the file has not been changed)
for [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
and [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) methods, then the server must return HTTP
status code 304 (Not Modified).

The comparison with the stored [`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) uses the _weak
comparison algorithm_, meaning two files can be considered identical if the content is equivalent — they don't have to
be identical byte for byte. For example, two files that differ by the date of generation could still be considered as
identical.

When used in combination
with [`If-Modified-Since`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since), `If-None-Match`
has precedence.

[Source: Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match)

## If-modified-since

The `If-Modified-Since` request HTTP header makes the request conditional: the server will send back the requested
resource, with a [`200`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) status, only if it has been last
modified after the given date. If the request has not been modified since, the response will be
a [`304`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304) without any body;
the [`Last-Modified`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified) response header of a
previous request will contain the date of last modification.

When used in combination with [`If-None-Match`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match)
, it is ignored, unless the server doesn't support `If-None-Match`.

The most common use case is to update a cached entity that has no
associated [`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag).

[Source: Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since)

## Supported APIs

* GTFS Regional
* GTFS Regional Realtime
* NeTEx Regional

## Read more

Conditional requests on
MDN: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional\_requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests)

ETag on
MDN: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)

If-None-Match on
MDN: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match)

If-Modified-Since on
MDN: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since)
