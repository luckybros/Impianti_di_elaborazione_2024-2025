function [t, empRel]=EmpiricalTTF(fileinter)
    interarrivals=load (fileinter)
    [y,t]=cdfcalc(interarrivals);
    empTTF=y(2:size(y,1));
    empRel=1-empTTF;
    plot(t,empTTF,'-*b',t,empRel,'-+r');
    xlabel('time [s]'); ylabel('p');
    legend('emp TTF', 'emp Rel');
end