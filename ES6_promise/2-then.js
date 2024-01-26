export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      const response = { status: 200, body: 'success' };
      return (response);
    })
    .catch(() => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
