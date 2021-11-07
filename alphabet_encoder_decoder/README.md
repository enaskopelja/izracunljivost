# Alphabet encoder/decoder

## Zadatak
> U po volji odabranom programskom jeziku napišite enkoder (ako Vam je JMBAG//10 paran) odnosno dekoder (JMBAG//10 neparan) skupa Σ*.
>
> Oba programa trebaju omogućiti unos abecede (najbolje kao string bez ikakvog separatora, recimo {a,b,c} se unosi kao abc). 
> 
> Enkoder treba uz to pitati za neku riječ w nad tom abecedom, te izračunati i ispisati njen kod ⟨w⟩. 
> 
> Dekoder treba pitati prirodni broj te ispisati riječ nad Σ čiji je to kod. 
> 
> Smijete pretpostaviti da abeceda neće imati duplikata u sebi, ali kodiranje mora ići redoslijedom kojim je abeceda 
> navedena (npr. "cab" znači da se b kodira brojem 3). Bilo bi lijepo prijaviti grešku ako riječ sadrži slovo koje 
> nije u abecedi, ali nije nužno (normalni programski jezici će to ionako obaviti za vas;).
>
> Predajte izvorni kod (za kompajlirane jezike možete i izvršnu datoteku, ali izvorni kod je obavezan). 
> Programi moraju raditi za kodove do 2^31-1 (bilo bi super ako rade i za veće kodove, ali ne morate se mučiti oko toga).


# Enkoder:

`python3 encode.py --alphabet ${ALPHABET}`

# Dekoder:

`python3 decode.py --alphabet ${ALPHABET}`