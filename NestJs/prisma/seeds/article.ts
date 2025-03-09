import { PrismaClient } from "@prisma/client";
import { Random } from "mockjs";
import { create } from "../helper";

export function article() {
    create(10, async (prisma: PrismaClient) => {
        await prisma.article.create({
            data: {
                title: Random.ctitle(),
                content: Random.cparagraph(10, 50),
                thumb: Random.image("200x200"),
                categoryId: Random.integer(1, 5),
            },
        });
    })
}