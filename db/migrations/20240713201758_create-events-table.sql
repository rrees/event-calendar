-- migrate:up

CREATE TABLE IF NOT EXISTS events(
	id SERIAL PRIMARY KEY,
	external_id UUID NOT NULL default gen_random_uuid (),
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	name TEXT UNIQUE NOT NULL,
	url TEXT,
	comment TEXT,
	created timestamp NOT NULL default current_timestamp,
	updated timestamp NOT NULL default current_timestamp
);

CREATE INDEX IF NOT EXISTS event_end_date_idx
ON events (end_date);

CREATE OR REPLACE FUNCTION update_modified_column() 
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified = now();
    RETURN NEW; 
END;
$$ language 'plpgsql';

CREATE TRIGGER update_events_modtime
BEFORE UPDATE ON events
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();


-- migrate:down

DROP INDEX IF EXISTS event_end_date_idx;

DROP TABLE IF EXISTS events;

DROP TRIGGER IF EXISTS update_events_modtime ON events;

DROP FUNCTION IF EXISTS update_modified_column;