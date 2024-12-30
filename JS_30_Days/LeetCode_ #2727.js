/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
  // Check if the object is empty
  return Object.keys(obj).length === 0;
};


isEmpty({}); // true
isEmpty({ key: "value" }); // false
isEmpty([]); // true
isEmpty([1, 2, 3]); // false
