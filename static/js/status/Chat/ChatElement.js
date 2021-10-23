import {StatusElement} from "../StatusElement.js";

export class ChatElement extends StatusElement {
    constructor(data) {
        super(data);
        this.element = this.drawElement();
        this.div = this.drawElement();
        this.dataElement = undefined;
    }

    refreshTime() {
        if (!this.dataElement) {
            this.dataElement = $(`#message-timestamp-${this.data.id}`);
        }
        let timeText = super.generateReadableTime();
        this.dataElement.text(timeText);
    }

    drawElement() {
        return $(
            `
            <div class="d-flex mb-3 m-2 chat-message">
                <div>
                    <img class="rounded-circle m-3 chat-icon" src="${this.data.author.image}"
                     alt="${this.data.author.name}">
                </div>
                <div class="w-100">
                    <h6 class="card-title p-0 m-0">${this.data.author.username}</h6>
                    <p class="text-justify m-0" style="word-break: break-all">${this.data.body}</p>
                    <h6 class="card-title text-right pt-1" id="message-timestamp-${this.data.id}"
                     style="font-size: smaller;">
                        ${super.generateReadableTime()}
                    </h6>
                </div>
            </div>
        `
        )
    }

}