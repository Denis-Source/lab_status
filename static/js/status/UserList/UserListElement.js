import {StatusElement} from "../StatusElement.js";


export class UserListElement extends StatusElement {
    constructor(data) {
        super(data);
        this.dataElement = undefined;
        this.selector = `#${this.data.username}-row`;
    }

    refreshTime() {
        if (!this.dataElement) {
            this.dataElement = $(`#user-date-${this.data.id}`);
        }
        let timeText = super.generateReadableTime();
        this.dataElement.text(timeText);
    }

    drawElement() {
        return $(
            `
            <tr id="${this.data.username}-row">
                <td style="vertical-align: middle; width: 50px">
                <p class="m-2">
                    <img class="rounded-circle chat-icon" src="${this.data.image}" alt="${this.data.username}">
                </p>
                </td>
                <td style="vertical-align: middle">
                    <p class="m-2">${this.data.first_name} ${this.data.last_name}</p>
                </td>
                <td style="vertical-align: middle"><p class="m-2">${this.data.position}</p></td>
                <td style="vertical-align: middle">
                    <p id="user-date-${this.data.id}" class="m-2">
                    ${moment(this.data.last_time_status_changed).fromNow()}
                    </p>
                </td>
            </tr>   
            `
        )
    }
    removeElement() {
        $(this.selector).remove();
    }
}