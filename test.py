from sentiment import TwitterSentiment

twitter = TwitterSentiment()
test_list = [
	'Court affirmed 4th Amendment protections against NSA\'s mass surveillance, defending "the right to be left alone."',
	'Germany spies among friends: controversy grows over espionage activities http://dw.com/p/1H4Hx  #NSA',
	'Is the NSA Using Zero-Day Exploits before Reporting Them? https://hacked.com/nsa-using-zero-day-exploits-reporting/ … #Bitcoin ',
	'This story piqued our interest because NSA isn\'t our usual criminal informant...  #ChicagoPD',
	'Appeals Court Says NSA Can Keep Trampling 4th Amendment With Phone Surveillance Program For Now http://goo.gl/fb/YL5Ay8 ',
	'Judge Orders #NSA to Stop Collecting Call Records — Another BIG Win for #Privacy Advocates http://www.usnews.com/news/articles/2015/11/09/judge-orders-nsa-to-stop-collecting-call-records … … ',
	'nowden Vindicated as Judge Shuts Down NSA Bulk Spying in Epic Smackdown http://theantimedia.org/snowden-vindicated-as-judge-shuts-down-nsa-bulk-spying-in-epic-smackdown/ …',
	'A US judge’s ruling against the NSA is a big win for Edward Snowden http://qz.com/545978/a-federal-judges-ruling-against-the-nsa-is-a-big-win-for-edward-snowden/ …',
	'Weeks before NSA bulk phone spying ends, US judge (kinda) reins in program http://arstechnica.com/tech-policy/2015/11/weeks-before-nsa-bulk-phone-spying-ends-us-judge-kinda-reins-in-program/ … by @dmkravets',
	'ICYMI, federal judge ruled that NSA’s phone records collection program violates the Constitution http://bit.ly/1NG6bmY '
]

print(twitter.get_sentiment(test_list))

