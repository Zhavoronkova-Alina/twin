# Twin arithmetic class in Python
A Python module that implements twin arithmetic.
## Operations with twins
Twin is a couple of intervals $T=(X_l,X)$, where $X_l,X \in \mathbb{IR}$.

Estimate an unknown interval 𝐼 as a twin means to find such a twin $T=(X_l,X)$: $X_l \subseteq I \subseteq X$ ($I \sqsubseteq T$).

$T_1=(\[a^-, a^+\], \[A^-, A^+ \])$
$T_2=(\[b^-, b^+\], \[B^-, B^+ \])$

Define the numbers p and q as follows:
- if $\[a^-, a^+\] \neq \varnothing$ and $\[b^-, b^+\] \neq \varnothing$
$$p=\min{(a^-+B^+, b^-+A^+)}$$
$$q=\max{(a^++B^-, b^++A^-)}$$
- if $\[a^-, a^+\] = \varnothing$ and $\[b^-, b^+\] \neq \varnothing$
$$p=b^-+A^+$$
$$q= b^++A^-$$
- if $\[a^-, a^+\] \neq \varnothing$ and $\[b^-, b^+\] = \varnothing$
$$p=a^-+B^+$$
$$q=a^++B^-$$
- if $\[a^-, a^+\] = \varnothing$ and $\[b^-, b^+\] = \varnothing$

$p,q$ is undefined

Define the functions $\varphi$ and $\psi$ as follows:

$Z$ is empty set or it have one element, $I_1,I_2 \in \mathbb{IR}$.
- if $I_1 \cap I_2=Z$: 
$$\varphi(I_1,I_2)= min_{\subseteq}{( (c^-,c^+) | (c^- \in I_1 \text{ and } c^+ \in I_2) \vee  (с^- \in I_2 \text{ and }  c^+ \in I_1))}$$
- else
 $$\varphi(I_1,I_2)=\varnothing$$
 
 $$\psi(I_1,I_2)=max_{\subseteq} ( (c^-,c^+) |c^-,c^+ \in I_1 \cup I_2 )$$
### Sum
Let's define inner length of twin as $|T|_l =\|X_l\|$ and outer length as $|T| =\|X\|$. 
If $I \sqsubseteq (\varnothing, X)$ than $|T|_l = -1$. It means that exist only outer estimation.
Than
- if $|T_1| \leq |T_2|_l \vee |T_2| \leq |T_1|_l$
$$T_1+T_2= ( (p,q), (A-+B^-,A^++B^+) )$$
- else
$$T_1+T_2= ((\varnothing), (A-+B^-,A^++B^+) )$$
### Mul
Multiplication of two twins $T_1,T_2$
- if $|T_1| \neq -1$ and $|T_2|_l \neq -1$, then
$$T_1 \cdot T_2 = (\psi(\varphi(a^-(B^-,B^+), a^+(B^-,B^+)),\varphi(b^- (A^-,A^+), b^+  (A^-,A^+) ) )  , (A^-, A^+)\cdot (B^-,B^+) )$$
- if $|T_1| = -1$ and $|T_2|_l \neq -1$, then
$$T_1 \cdot T_2 = ( \varphi(b^- (A^-,A^+), b^+  (A^-,A^+) ) , (A^-, A^+) \cdot (B^-,B^+) )$$
- if $|T_1| \neq -1$ and $|T_2|_l = -1$, then
$$T_1 \cdot T_2 =( \varphi(a^- (B^-,B^+), a^+   (B^-,B^+) ) , (A^-, A^+) \cdot (B^-,B^+) ) $$
- if $|T_1| = -1$ and $|T_2|_l = -1$, then
$$T_1 \cdot T_2 = (\varnothing,(A^-, A^+)\cdot (B^-,B^+) )$$

### Uminus 
$$-T_1=(-X_l,-X)$$
### Opposite element
$$ 1 / T_1 = ( 1 / X_l , 1 / X )$$

## Order relation

