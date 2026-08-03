# Self Review

The evening after I submitted this repo, my mind returned to my work. In particular the way I'd conflated enabling "chaos mode" with the required api-key. At the time I felt it was best to radically accept my submission as-is/was, and leave it there.

The thoughts didn't stop though. The following day I pulled at that thread of thinking, and identified a few key areas in which my submission fell short.

**My takeaway:** my submission was not reflective of my capabilities.


## Action

I realised I could take action: it's my repsitory after all! 

**Key Problems:** Showing intent; conflated concerns; service isolation

## Plan

Remediation items:

- Quote risk band: risk band not used in quote generation. comments and unit tests can show intent.
- Chaos mode: as its own http header (requiring valid api-key). separates concerns.
- Config from env (including chaos mode). separate configuration from code.
- Review service boundaries. be explicit about what's shared and what isn't, and what shouldn't be shared.
- comments: the code is completely uncommented (especially key decisions/tradeoffs; validation message parsing is gross)
- Readme AI usage: did not use AI for pre-submission review; sdd roadmap as north-star, specs as context
- adrs / decisions: state why choices have been made e.g. tradeoffs, options

## Migraine strikes

Unfortunately, I suffered from a migraine from early Friday until Sunday, which has delayed any action. Even so, I plan to at least share this self review and implement my identified remediation items.

# Execution

## Risk band

Quote derivation does not use the supplied risk band. While the current implementation is very straightforward, the underlying intention is lacking: was this an oversight or by design?

Unit tests are a great way to show intent of the subject [under test]. I've chosen this approach to showing my intent that right now, the risk band does not factor into the total commission for the quote.

## Chaos mode

The initial implementation overloaded the api key concept with chaos mode: api keys could be defined as 'chaotic'. I had discounted the option of "chaos for all" via an environmental toggle (e.g. when `env == DEVELOPMENT`) as I really value being able to inject a "poison pill" type request into an abrtitrary runtime under controlled conditions. 

This can yeild great insight, especially when dealing with distributed systems or crossing substantial system boundaries.

To that point, the API now determines whether the request is 'chaotic' via a HTTP request header: `X-Bendigo-Chaos'. This check is performed after the api key has been validated.