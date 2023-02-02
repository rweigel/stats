diary('probability_brute_force_ordered_2_tuples.log')

na = 3;
nb = 2;
N = 0;
for a = 1:na
   for b = 1:nb
      fprintf('(%d,%d)\n',a,b);
      N = N + 1;
   end
end
fprintf('Number of unique ordered tuples = %d\n',N);

fprintf('----------')

G = {'Bob','Joe','Don'};
B = {'Sue','Ali','Jen','Kat'};
N = 0;
for g = 1:length(G)
   for b = 1:length(B)
      fprintf('(%s,%s)\n',G{g},B{b});
      N = N + 1;
   end
end
fprintf('Number of unique ordered tuples = %d\n',N);
diary off
