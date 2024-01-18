import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqlf, floors) {
    super(sqlf);
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    this._floors = value;
  }

  evacutionWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
