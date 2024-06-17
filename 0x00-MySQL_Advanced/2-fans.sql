-- An SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SET @rank=0;
SELECT 
  origin, 
  nb_fans, 
  @rank:=@rank+1 as rank
FROM 
  metal_bands
ORDER BY 
  nb_fans DESC;
