function createInt8TypedArray(length, position, value) {
  if (value == null) {
    throw Error('Position outside range');
  } else {
    const buffer = new ArrayBuffer(length);
    const int8 = new Int8Array(buffer);
    int8[position] = value;
    return new DataView(buffer);
  }
}

export default createInt8TypedArray;
