/**
 * @param {number} millis
 * @return {Promise<void>}
 */
function sleep(millis) {
    return new Promise((resolve) => {
        setTimeout(resolve, millis);
    });
}

// Example usage:
const t = Date.now();
sleep(1000).then(() => console.log(`Elapsed time: ${Date.now() - t}ms`));

// Async/Await example:
async function testSleep() {
    const t = Date.now();
    await sleep(2000);
    console.log(`Elapsed time: ${Date.now() - t}ms`);
}

testSleep();
