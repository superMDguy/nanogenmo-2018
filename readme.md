# NaNoGenMo 2018

I'm going to put all my work for [NaNoGenMo 2018](https://github.com/NaNoGenMo/2018) in this repo. I have a ton of ideas, which I listed [here](https://github.com/NaNoGenMo/2018/issues/22), and I'm not sure how much time I'll end up having. I'm just going to go through a few of my ideas, and see how far I get.


## Sentence Vector Translation
[Code](./Sentence%20Change.ipynb) | [Novel](./Northanger_Abbey_x_Doyle.pdf)

### Explanation
For each sentence in book _A_, find the semantically closest sentence in a book _B_, using cosine distance between [InferSent](https://github.com/facebookresearch/InferSent) sentence vectors.

### Sample
Northanger Abbey, built with sentences from Winston Churchill. Original in italics, translated below.

_CHAPTER 1  No one who had ever seen Catherine Morland in her infancy would have supposed her born to be an heroine._<br/> Everything which the girl said seemed to be meant as an insult to me, and yet I could not imagine how I had ever offended her.

_Her situation in life, the character of her father and mother, her own person and disposition, were all equally against her._<br/>Her whole life was a round of devotion and of love, which was divided between her husband and her only son, Harold.

_Her father was a clergyman, without being neglected, or poor, and a very respectable man, though his name was Richard-- and he had never been handsome._<br/>`` You must know, Sir Charles, that though my son knew nothing of his parents, we were both alive, and had never lost sight of him.

_He had a considerable independence besides two good livings-- and he was not in the least addicted to locking up his daughters._<br/>Now that they had not only ceased to protect him, but had themselves become a source of trouble to him, he began to understand how great the blessing was which he had enjoyed, and to sigh for the happy days before his girls had come under the influence of his neighbor.

_Her mother was a woman of useful plain sense, with a good temper, and, what is more remarkable, with a good constitution._<br/>In her pure and earnest mind her mother's memory was enshrined as that of a saint, and the thought that any one should take her place seemed a terrible desecration.

_She had three sons before Catherine was born; and instead of dying in bringing the latter into the world, as anybody might expect, she still lived on-- lived to have six children more-- to see them growing up around her, and to enjoy excellent health herself._<br/>He was married to the second daughter of Sir James Ovington; and as I have seen three of his grandchildren within the week, I fancy that if any of Sir Lothian's descendants have their eye upon the property, they are likely to be as disappointed as their ancestor was before them.
