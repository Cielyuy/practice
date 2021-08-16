clc
clear
path = uigetdir;
suffix=['p';'v'];
for j=1:length(suffix);
    str=strcat('-',suffix(j),'.txt');
    A = dir([path,'\','*',str]);
    for i = 1:size(A,1)
        %          name{i} = ['n',num2str(i),str];
        %
        %           A=isstrprop(str,'digit');
        % B=str(A);
        % C=str2num(B)
        name_str = A(i,1).name;
        %           datapath = [path,'\',name{i}];
        datapath = [path,'\',name_str];
        DATA = importdata(datapath);
        DATA = DATA.data;
        num_i=isstrprop(name_str,'digit');
        name_i = name_str(num_i);
        name_j =str2num(name_i);
        R(2:size(DATA,1)-1,name_j) = DATA(3:end,3);
        R(1,name_j) = name_j;
        clear DATA;
    end
    xlswrite([path,'\pvxyz.xlsx'],R,suffix(j));
end
vi=['vx';'vy';'vz'];
for j=1:length(vi);
    str=strcat('-',vi(j,:),'.txt');
    A = dir([path,'\','*',str]);
    for i = 1:size(A,1)
        %          name{i} = ['n',num2str(i),str];
        %           datapath = [path,'\',name{i}];
        name_str = A(i,1).name;
        datapath = [path,'\',name_str];
        DATA = importdata(datapath);
        DATA = DATA.data;
        num_i=isstrprop(name_str,'digit');
        name_i = name_str(num_i);
        name_j =str2num(name_i);
        %           R(2:size(DATA,1)-1,i) = DATA(3:end,3);
        %           R(1,i) = i;
        R(2:size(DATA,1)-1,name_j) = DATA(3:end,3);
        R(1,name_j) = name_j;
        
        clear DATA;
    end
    xlswrite([path,'\pvxyz.xlsx'],R,vi(j,:));
end
disp('**************Done***************')