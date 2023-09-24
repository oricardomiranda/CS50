SELECT people.name
FROM people
WHERE people.phone_number IN (
	SELECT receiver
	FROM phone_calls
	WHERE year = 2021 AND month = 7 AND day = 28
	AND duration < 60
	AND caller = (
	SELECT people.phone_number
        FROM people
        WHERE people.name = "Bruce"
    )
);
