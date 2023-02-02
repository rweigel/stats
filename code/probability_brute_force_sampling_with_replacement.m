clear;
set(groot,'defaultAxesFontName','Times')
set(groot,'defaultAxesFontSize',16)

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

ts = sprintf('Number of unique results in %d experiments: %d\n',Ne,Nu);

colormap(parula(6));
image(lists);
title(ts,'FontWeight','normal')
cb = colorbar();
set(gca,'XTick',[1,2,3]);
xlabel('Roll number');
ylabel('Experiment number');
set(get(cb,'Title'),'String','Roll value');
set(cb,'YTick',1.5:6.5);
set(cb,'YTickLabel',[1:6]);

fprintf('Saving probability_brute_force.{png,pdf}\n');
print -dpng -r300 probability_brute_force.png
print -dpng -r300 probability_brute_force.pdf
fprintf('Saved probability_brute_force.{png,pdf}\n');
