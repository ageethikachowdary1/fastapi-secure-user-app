const { test, expect } = require('@playwright/test');

const uniqueId = Date.now();

test('register with valid data', async ({ page }) => {
  await page.goto('/static/register.html');
  await page.fill('#username', `playuser${uniqueId}`);
  await page.fill('#email', `playuser${uniqueId}@example.com`);
  await page.fill('#password', '123456');
  await page.fill('#confirmPassword', '123456');
  await page.click('button[type="submit"]');
  await expect(page.locator('#message')).toHaveText('Registration successful');
});

test('register with short password', async ({ page }) => {
  await page.goto('/static/register.html');
  await page.fill('#username', `shortuser${uniqueId}`);
  await page.fill('#email', `shortuser${uniqueId}@example.com`);
  await page.fill('#password', '123');
  await page.fill('#confirmPassword', '123');
  await page.click('button[type="submit"]');
  await expect(page.locator('#message')).toHaveText('Password must be at least 6 characters long');
});

test('login with correct credentials', async ({ page }) => {
  await page.goto('/static/register.html');
  await page.fill('#username', `loginuser${uniqueId}`);
  await page.fill('#email', `loginuser${uniqueId}@example.com`);
  await page.fill('#password', '123456');
  await page.fill('#confirmPassword', '123456');
  await page.click('button[type="submit"]');
  await expect(page.locator('#message')).toHaveText('Registration successful');

  await page.goto('/static/login.html');
  await page.fill('#email', `loginuser${uniqueId}@example.com`);
  await page.fill('#password', '123456');
  await page.click('button[type="submit"]');
  await expect(page.locator('#message')).toHaveText('Login successful');
});

test('login with wrong password', async ({ page }) => {
  await page.goto('/static/login.html');
  await page.fill('#email', `loginuser${uniqueId}@example.com`);
  await page.fill('#password', 'wrong123');
  await page.click('button[type="submit"]');
  await expect(page.locator('#message')).toHaveText('Invalid credentials');
});
