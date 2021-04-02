function Aprime = tensortransform(A, Q)
  Aprime = zeros(3,3);
  p = 1;
  q = 1;
  for i = 1:3
    for j = 1:3
      Aprime(i,j) = (Q(i,:)*(Q(j,:)*A)');
    endfor
  endfor
endfunction
