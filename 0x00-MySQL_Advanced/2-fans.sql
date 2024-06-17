-- An SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT
    origin,
    fans AS nb_fans,
    RANK() OVER (
        ORDER BY
            nb_fans DESC
    ) as rank
FROM
    metal_bands;
