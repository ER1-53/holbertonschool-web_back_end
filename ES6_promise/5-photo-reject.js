export default function uploadPhoto(filename) {
  return new Promise(((resolve, reject) => {
    if (typeof filename === 'string') {
      reject(Error(`${filename} cannot be processed`));
    }
  }));
}
