import {Chat} from "./Chat/Chat.js";
import {ActivityFeed} from "./ActivityFeed/ActivityFeed.js";
import {UserList} from "./UserList/UserList.js";
import {PartsStatus} from "./PartsStatus/PartsStatus.js";

export class Status {
    constructor(csrf) {
        this.csrf = csrf;
        this.activityContainer = new ActivityFeed();
        this.chat = new Chat(this.csrf);
        this.userList = new UserList();
        this.partStatus = new PartsStatus(this.csrf);
    }

    draw() {
        this.activityContainer.draw();
        this.chat.draw();
        this.userList.draw();
        this.partStatus.draw();
    }
}