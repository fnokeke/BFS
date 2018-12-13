# BFS Project
Development of a Beneficiary Feedback System (BFS) for collecting feedback from care recipients who receive services from Community Health Workers in low-resource settings.

![App screenshot 1](ussd-shot1.png) ![App screenshot 2](ussd-shot2.png)

# Publication
Fabian Okeke, Lucas Nene, Anne Muthee, Stephen Odindo, Dianna Kane, Isaac Holeman, and Nicola Dell.
[Challenges and Opportunities in Connecting Care Recipients to the Community Health Feedback Loop](http://nixdell.com/papers/2018-ictd-bfs.pdf).
International Conference on Information and Communication Technologies and Development (ICTD 2019).
[pdf](http://nixdell.com/papers/2018-ictd-bfs.pdf).

# Libraries
[ussd_airflow](https://github.com/mwaaas/ussd_airflow)

# Test in Simulator
- Launch Africa's Talking Simulator [example](https://simulator.africastalking.com:1517/simulator/ussd)
- Enter Country / Phone (e.g. Kenya / +254-7-123-456-789)
- Enter ussd code `*384*11100#` and then call button
- USSD screen sessions will appear
- Congrats!

# Change Screen Content
- Modify [screens.yml file in this repo](https://github.com/fnokeke/BFS/blob/master/UssdApp/static/screens.yml)
- [Check here](https://django-ussd-airflow.readthedocs.io/en/latest/tutorial.html) for more information on creating ussd screens


