import { user } from "./seeds/user";
import { category } from "./seeds/category";
import { article } from "./seeds/article";

async function main() {
    user();
    await category();
    article();
}

main()