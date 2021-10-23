export class StatusElement {
    constructor(data) {
        this.data = data;
    }

    generateReadableTime() {
        return moment(this.data.time).fromNow()
    }

}