-- migrate:up

ALTER TABLE events
ALTER id
DROP DEFAULT;

DROP SEQUENCE IF EXISTS events_id_seq;   

ALTER TABLE events
ALTER COLUMN id
ADD GENERATED ALWAYS AS IDENTITY
(RESTART WITH 3);

CREATE UNIQUE INDEX IF NOT EXISTS evt_public_id_idx 
ON events (external_id);

ALTER TABLE events
ADD CONSTRAINT evt_public_id_uq
UNIQUE USING INDEX evt_public_id_idx;



-- migrate:down

DROP INDEX IF EXISTS evt_public_id_idx;

ALTER TABLE events
DROP CONSTRAINT evt_public_id_uq;
