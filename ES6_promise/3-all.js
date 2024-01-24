import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([uploadPhoto, createUser]) => {
      console.log(uploadPhoto.body, createUser.firstName, createUser.lastName);
    })
    .catch((error) => {
      console.log('Signup system offline');
    });
}
/* .then(values => {
			console.log(values[0].body, values[1].firstName, values[1].lastName)
		})
		Car then prend un tableau d'estructuré [ ] voir cours sur les array */
