# NaNoGenMo 2018

I'm going to put all my work for [NaNoGenMo 2018](https://github.com/NaNoGenMo/2018) in this repo. I have a ton of ideas, which I listed [here](https://github.com/NaNoGenMo/2018/issues/22), and I'm not sure how much time I'll end up having. I'm just going to go through a few of my ideas, and see how far I get.


## Sentence Vector Translation
[Code](./Sentence Change.ipynb) | Novel WIP

### Explanation
For each sentence in book _A_, find the semantically closest sentence in a book _B_, using cosine distance between [InferSent](https://github.com/facebookresearch/InferSent) sentence vectors.

### Sample
_Lincoln's "Gettysburg Address" with sentences from Winston Churchill_

> One November day nearly two years after my admission as junior member of the firm of Watling, Fowndes and Ripon seven gentlemen met at luncheon in the Boyne Club; Mr. Barbour, President of the Railroad, Mr. Scherer, of the Boyne Iron Works and other corporations, Mr. Leonard Dickinson, of the Corn National Bank, Mr. Halsey, a prominent banker from the other great city of the state, Mr. Grunewald, Chairman of the Republican State Committee, and Mr. Frederick Grierson, who had become a very important man in our community. 
> 
>  IV 
> 
>  I come home impressed with the fact that Britain has learned more from this war than any other nation, and will probably gain more by that knowledge. How excellently they would have agreed on the general question of the war! 
> 
>  Yes, the dream of that youth had been to benefit in some way that community in which circumstances had decreed that he should live, and in this connection it might not be out of place to mention a bill then before the Legislature of the state, now in session. To think that you should be reduced to that, and I not know it!" 
> 
>  "Well," said Fowndes, "there's an element of risk in such a proceeding I need not dwell upon." But most men of his type have seen them in despair; and since he was not related to this particular despair, what finer feelings he had were the more easily aroused. "It was mean, not to tell you, but I'd never had anything like this -- what you were giving me -- and I wanted all I could get." 
> 
>  Some faith indeed had given him strength to renounce those things in life I had held dear, driven him on to fight until his exhausted body failed him, and even now that he was physically helpless sustained him. If we should obtain a majority at the next election -- and I have good hopes that if we act with wisdom and with union, and, above all, with courage, we shall undoubtedly obtain an effective majority -- the prize we shall claim will be a final change in the relations of the two Houses of Parliament, of such a character as to enable the House of Commons to make its will supreme within the lifetime of a single Parliament; and except upon that basis, or for the express purpose of effecting that change, we will not accept any responsibility for the conduct of affairs. 
> 
> 
