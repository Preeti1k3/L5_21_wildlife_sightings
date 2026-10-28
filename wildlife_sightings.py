"""Record and summarize wildlife sightings."""

import hashlib
import sqlite3

db_connection = sqlite3.connect(":memory:")
db_connection.execute(
    "CREATE TABLE sightings (id INTEGER PRIMARY KEY, "
    "species TEXT, zone TEXT, count INTEGER)"
)


def log_sighting(conn, species, zone, count, extras=None):
    """Record a wildlife sighting and update species totals."""
    if extras is None:
        extras = {}

    conn.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count)
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Generate a short identifier for a wildlife observer."""
    return hashlib.sha256(observer.encode()).hexdigest()[:6]


def zone_summary(conn, zone):
    """Return the total number of sightings recorded in a zone."""
    row = conn.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?", (zone,)
    ).fetchone()

    if row[0] is None:
        return 0
    return row[0]


def rarest(conn):
    """Return the species with the lowest total sighting count."""
    rows = conn.execute(
        "SELECT species, SUM(count) FROM sightings GROUP BY species"
    ).fetchall()

    if not rows:
        return None

    rarest_sighting = min(rows, key=lambda row: row[1])
    return rarest_sighting[0]


def main():
    """Run sample wildlife sightings and print summary results."""
    totals = log_sighting(db_connection, "Leopard", "North", 1)
    log_sighting(db_connection, "Chital", "North", 24, totals)
    log_sighting(db_connection, "Hornbill", "East", 3, totals)

    if len(totals) != 3:
        raise ValueError("Expected exactly three species in totals.")

    print(
        observer_id("Arun"),
        zone_summary(db_connection, "North"),
        rarest(db_connection),
    )


if __name__ == "__main__":
    main()