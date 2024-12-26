var TimeLimitedCache = function () {
  this.cache = new Map(); // Stores key-value pairs along with expiration times
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration - Time until expiration in milliseconds
 * @return {boolean} - Returns true if the key already exists and has not expired, false otherwise
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  const currentTime = Date.now();
  const existing = this.cache.get(key);

  if (existing && existing.expirationTime > currentTime) {
    this.cache.set(key, { value, expirationTime: currentTime + duration });
    return true;
  }

  this.cache.set(key, { value, expirationTime: currentTime + duration });
  return false;
};

/** 
 * @param {number} key
 * @return {number} - Returns the value associated with the key if it hasn't expired, -1 otherwise
 */
TimeLimitedCache.prototype.get = function (key) {
  const currentTime = Date.now();
  const existing = this.cache.get(key);

  if (existing && existing.expirationTime > currentTime) {
    return existing.value;
  }

  this.cache.delete(key); // Clean up expired keys
  return -1;
};

/** 
 * @return {number} - Returns the count of non-expired keys in the cache
 */
TimeLimitedCache.prototype.count = function () {
  const currentTime = Date.now();
  let validKeys = 0;

  for (const [key, { expirationTime }] of this.cache) {
    if (expirationTime > currentTime) {
      validKeys++;
    } else {
      this.cache.delete(key); // Remove expired keys
    }
  }

  return validKeys;
};

/**
 * Example usage:
 * const timeLimitedCache = new TimeLimitedCache();
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1); // 42
 * timeLimitedCache.count(); // 1
 */
