import nltk

def sentence_features(si, ix):
	d_ft = {}
	d_ft['word'] = st[ix]
	d_ft['dist_from_first'] = ix - 0
	d_ft['dist_from_last'] = len(st) - ix
	d_ft['capitalized'] = st[ix][0].upper() == st[ix][0]
	d_ft['prefix1'] = st[ix][0]
	d_ft['prefix2'] = st[ix][:2]
	d_ft['prefix3'] = st[ix][:3]
	d_ft['suffix1'] = st[ix][-1]
	d_ft['suffix2'] = st[ix][-2:]
	d_ft['suffix3'] = st[ix][-3:]
	d_ft['prev_word'] = '' if ix==0 else st[ix-1]
	d_ft['next_word'] = '' if ix==(len(st)-1) else st[ix+1]
	d_ft['numeric'] = st[ix].isdigit()

	return d_ft

def ext_ft(tg_sent):
	sent, tag = [], []

	for tg in tg_sent:
		for index in range(len(tg)):
			sent.append(sentence_features(get_untagged_sentence(tg), index))
			tag.append(tg[index][1])


	return sent, tg



tagged_sentence = nltk.corpus.treebank.tagged_sents(tagset='universal')

X,y = ext_ft(tagged_sentence)
