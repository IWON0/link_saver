SELECT u.id,
       u.email,
       u.date_joined,
       COUNT(l.id) AS links_count
FROM users_user u
LEFT JOIN links_link l ON u.id = l.user_id
GROUP BY u.id, u.email, u.date_joined
ORDER BY links_count DESC, u.date_joined ASC
LIMIT 10;
