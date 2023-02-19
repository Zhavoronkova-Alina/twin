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
$$\varphi(I_1,I_2)=\begin{cases}
   \min_{\subseteq} \{ \[c^-,c^+\] | (c^- \in I_1 & c^+ \in I_2) \vee (с^- \in I_2 & c^+ \in I_1) \}, & if I_1 \cap I_2 =Z;\\ 
   \varnothing,& else
 \end{cases}$$

### Sum
$T_1+T_2=$

### Mul

### Uminus

## Order relation

