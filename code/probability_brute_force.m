clear

% Number of experiments of rolling a die 3x in a row an writing
% down results.
Ne = 1000; 

for s = 1:Ne
    % randi(N,1) returns a randomly selectred value from integers
    % 1, ..., N. Could also use list = randi(6,[1,3]).
    list(1) = randi(6,1);
    list(2) = randi(6,1);
    list(3) = randi(6,1);

    lists(s,:) = list;
end

unique_lists = unique(lists,'rows');

Nu = size(unique_lists,1);

fprintf('Number of unique results in %d experiments: %d\n',Ne,Nu);
image((lists-1)/5)
colorbar