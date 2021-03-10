
max_dt = 5;
clear s_sim c2d mse iou
for dt = 1:max_dt
    for i = 1:(N_IMG-dt)
        t1    = tforms_dense(i).invert;
        trel  = affine2d(tforms_dense(i+dt).T*t1.T);
        W  = imwarp(imgaussfilt(adapthisteq(I{i+dt}(:,:,1),'Distribution','Rayleigh'),2),trel,'OutputView',imref2d(IM_RES));
        Wm = imwarp(Imask,trel,'OutputView',imref2d(IM_RES));
        wmask = boolean(Wm.*Imask);
        ROI(1,1) = find(max(wmask,[],2)==1,1,'first') + floor(IM_RES(1)*0.05);
        ROI(1,2) = find(max(wmask,[],2)==1,1,'last')  - floor(IM_RES(1)*0.05);
        ROI(1,3) = find(max(wmask,[],1)==1,1,'first') + floor(IM_RES(2)*0.05);
        ROI(1,4) = find(max(wmask,[],1)==1,1,'last')  - floor(IM_RES(2)*0.05);  
        image1 = W;
        image2 = imgaussfilt(adapthisteq(I{i}(:,:,1),'Distribution','Rayleigh'),2);
        image1 = image1(ROI(1):ROI(2),ROI(3):ROI(4),1).*wmask(ROI(1):ROI(2),ROI(3):ROI(4));
        image2 = image2(ROI(1):ROI(2),ROI(3):ROI(4),1).*wmask(ROI(1):ROI(2),ROI(3):ROI(4));
        
        imwrite(image1,strcat('eval_vis/image1_dt_',num2str(dt),'_i_',num2str(i),'.png'))
        imwrite(image2,strcat('eval_vis/image2_dt_',num2str(dt),'_i_',num2str(i),'.png'))
        
        seg1  = imwarp(S{i+dt},trel,'OutputView',imref2d(IM_RES));
        seg2  = S{i};
        
        imwrite(seg1,strcat('eval_vis/seg1_dt_',num2str(dt),'_i_',num2str(i),'.png'))
        imwrite(seg2,strcat('eval_vis/seg2_dt_',num2str(dt),'_i_',num2str(i),'.png'))
        
        s_sim{dt}(i) = ssim(image1,image2);
        mse{dt}(i) = immse(image1,image2);
        c2d{dt}(i) = corr2(image1,image2);       
        iou{dt}(i) = sum(sum((seg1>0.5).*(seg2>0.5).*wmask))/(sum(sum((seg1.*wmask)>0.5))+sum(sum((seg2.*wmask)>0.5)));
    end
end