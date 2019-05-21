
samples = 50;
t = [1:1:samples];

figure(1);
subplot(1,2,1);
plot(t, acc, '-b');
title('Training accuracy evolution');
xlabel('Epochs');
ylabel('Accuracy [0-1]');

subplot(1,2,2);
plot(t, loss, '-b');
title('Training losses evolution');
xlabel('Epochs');
ylabel('Losses');