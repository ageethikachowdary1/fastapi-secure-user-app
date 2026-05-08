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

test('calculation BREAD workflow', async ({ page }) => {
  await page.goto('/static/calculations.html');

  await page.fill('#addA', '10');
  await page.fill('#addB', '5');
  await page.selectOption('#addType', 'Add');
  await page.click('button:text("Add Calculation")');

  await expect(page.locator('#addMessage')).toContainText('Calculation added successfully');
  await expect(page.locator('#addMessage')).toContainText('Result: 15');

  const message = await page.locator('#addMessage').innerText();
  const match = message.match(/ID: (\d+)/);
  const calcId = match[1];

  await page.click('#browseButton');
  await expect(page.locator('#calculationList')).toContainText(`ID: ${calcId}`);

  await page.fill('#readId', calcId);
  await page.click('#readButton');
  await expect(page.locator('#readResult')).toContainText(`ID: ${calcId}`);

  await page.fill('#editId', calcId);
  await page.fill('#editA', '20');
  await page.fill('#editB', '4');
  await page.selectOption('#editType', 'Multiply');
  await page.click('button:text("Edit Calculation")');
  await expect(page.locator('#editMessage')).toContainText('Calculation updated successfully');
  await expect(page.locator('#editMessage')).toContainText('New result: 80');

  await page.fill('#deleteId', calcId);
  await page.click('#deleteButton');
  await expect(page.locator('#deleteMessage')).toContainText('Calculation deleted successfully');

  await page.fill('#readId', calcId);
  await page.click('#readButton');
  await expect(page.locator('#readResult')).toContainText('Calculation not found');
});

test('calculation divide by zero validation', async ({ page }) => {
  await page.goto('/static/calculations.html');

  await page.fill('#addA', '10');
  await page.fill('#addB', '0');
  await page.selectOption('#addType', 'Divide');
  await page.click('button:text("Add Calculation")');

  await expect(page.locator('#addMessage')).toHaveText('Cannot divide by zero');
});

test('calculation report dashboard loads report data', async ({ page }) => {
  await page.goto('/static/report.html');

  await page.click('button:text("Load Report")');

  await expect(page.locator('#report')).toContainText('Total Calculations');
  await expect(page.locator('#report')).toContainText('Average Result');
  await expect(page.locator('#report')).toContainText('Highest Result');
  await expect(page.locator('#report')).toContainText('Lowest Result');
  await expect(page.locator('#report')).toContainText('Add Count');
});
