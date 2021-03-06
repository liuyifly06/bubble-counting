% Analysis image with SVM Method
instanceSize = 20;
step = 4;
edge = 4;
scale = 70;
 
[trainInstances, trainLabels] = trainDataSetGeneration(instanceSize, step, edge, scale);

disp('SVM training ... ');
SVMModel = fitcsvm(trainInstances',trainLabels,'KernelFunction','rbf','KernelScale','auto','Prior',[0.98,0.02]);

% Batch Testing
DETECTOR_NUM=7; % number of detectors
NO_NUM = 6; % detctor 6 has only five experiments
ANGLE_NUM =3; % number of angles in taking images

index = 0;
manaul_count = [1 27 40 79 122 160 1 18 28 42 121 223 0 ...
        11 24 46 142 173 3 19 23 76 191	197 0 15 24 45 91 152 ...
        0 16 27	34 88 0	9 12 69	104 123];
data = manaul_count';

for det = 1:DETECTOR_NUM
        if(det == 6)
            num_n = NO_NUM-1;
        else
            num_n = NO_NUM;
        end
        for n = 0:(num_n-1)
            index = index+1;
            temp = zeros(ANGLE_NUM,1);
            for angle = 1:ANGLE_NUM  
                testfilename = ['../../images/detector_' num2str(det) '_no_' num2str(n) '_angle_' num2str(angle) '.jpg'];
                disp(['Processing ' testfilename ' ...']);
                testInstances = testDataSetGeneration(testfilename, instanceSize, step);
                [testingLabels, score] = predict(SVMModel,testInstances');
                temp(angle) = length(find(testingLabels>0));
                
                label_index = find(testingLabels<=0);
                resultShow = imread(testfilename);
                pr = 1:step:(size(resultShow,1)-instanceSize+1);
                pc = 1:step:(size(resultShow,2)-instanceSize+1);
                lr = length(pr);
                lc = length(pc);
                for i=1:length(label_index)
                    r = ceil(label_index(i)/lc);
                    c = label_index(i)-(r-1)*lc;
                    resultShow(pr(r):(pr(r)+instanceSize-1),pc(c):(pc(c)+instanceSize-1),:) = 0;
                end
                imwrite(resultShow,['../../images/svm/' 'detector_' num2str(det) '_no_' num2str(n) '_angle_' num2str(angle) '.jpg'],'jpg'); 
            end
            data(index,2) = mean(temp);
            data(index,3) = std(temp);
        end
end
save('data.txt','data','-ascii');