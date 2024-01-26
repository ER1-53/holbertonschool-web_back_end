import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
  return results.map((result) => ({
    status: result.status,
    value: result.status == 'fulfilled' ? result.value : `Error: ${result.reason}`,
  }));
}
