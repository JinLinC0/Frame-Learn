import { IsNotEmpty, Length } from 'class-validator';

export default class CreateArticleDto {
    @IsNotEmpty({ message: '标题不能为空' })
    @Length(1, 10, { message: '标题长度在1到10之间' })
    title: string;
    @IsNotEmpty({ message: '内容不能为空' })
    content: string;
}