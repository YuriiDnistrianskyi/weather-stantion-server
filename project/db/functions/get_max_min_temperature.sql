DROP FUNCTION IF EXISTS get_max_min_temperature;
CREATE FUNCTION get_max_min_temperature(get_weather_station_id INT)
    RETURNS JSON
    DETERMINISTIC
    BEGIN
        DECLARE max_temperature DECIMAL(5, 2);
        DECLARE min_temperature DECIMAL(5, 2);

        SELECT MAX(temperature), MIN(temperature)
        INTO max_temperature, min_temperature
        FROM Info
        WHERE DATE(_date) = CURDATE() AND weather_station_id = get_weather_station_id;

        RETURN JSON_OBJECT('max', max_temperature, 'min', min_temperature);
    END;
