# Redis session cache proposal

This change introduces Redis as a required session cache using `ioredis` and a mandatory `REDIS_URL` environment variable. PostgreSQL remains the primary database, while Redis stores application sessions.

The deployment must run Redis alongside PostgreSQL before the application starts.
