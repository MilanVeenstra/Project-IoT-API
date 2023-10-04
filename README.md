# API voor ons IoT eindproject

Vervang opnieuw < TIME >, < TEMPERATURE >, < DEPTH > en < id > met de gewenste waarden voor de meting.

Om een put request te posten naar de api via cmd, gebruik curl -X PUT -d "time=< TIME >&temperature=< TEMPERATURE >&depth=< DEPTH >" http://127.0.0.1:5000/data/meting_< id > gebruik put alleen als je super specifieke data wilt posten

Om een post request te doen naar de api via cmd, gebruik curl -X POST -d "time=< TIME >&temperature=< TEMPERATURE >&depth=< DEPTH >" http://127.0.0.1:5000/data je hoeft hier geen meting_id mee te geven want dat voert hij zelf al in

Om alle data op te vangen via de url kan je http://127.0.0.1:5000/data/all doen en als je een hele specifieke meting wilt hebben kan je http://127.0.0.1:5000/data/meting_< id > doen
