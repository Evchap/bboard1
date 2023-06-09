# План веб-сайта
Электронная доска объявлений позволит зарегистрированным пользователям публиковать объявления о продаже чего-либо. 

Объявления будут разноситься по рубрикам, структура рубрик будет иметь два уровня иерархии: 
на первом уровне расположатся рубрики общего плана ("недвижимость", "транспорт" и пр.),
а на втором - более конкретные ("жилье", "гаражи", "дачи", "легковой", "грузовой", "специальный").
Для вывода списка объявлений применяется пагинация, т. к. объявлений может оказаться очень много, и страница, содержащая все объявления, будет слишком большой. 
Также предусмотрена возможность поиска объявлений по введенному посетителем слову.
Под любым объявлением (на странице сведений об объявлении) может быть оставлено произвольное количество комментариев. 

Оставлять комментарии будет позволено любому пользователю, в том числе и гостю.

В составе объявления пользователь может поместить основную графическую иллюстрацию, которая будет выводиться и в списке объявлений, и в составе сведений
об объявлении, а также произвольное количество дополнительных иллюстраций, которые можно будет увидеть лишь на странице сведений об объявлении.
И основная, и дополнительные иллюстрации не являются обязательными к размещению.

Процедура регистрации нового пользователя на сайте будет разбита на два этапа.
На первом этапе посетитель вводит свои данные на странице регистрации, после
чего на указанный им адрес электронной почты приходит письмо с гиперссылкой, ведущей на страницу активации. 
На втором этапе посетитель переходит по гиперссылке, полученной в письме, попадает на страницу активации и становится полноправным пользователем.

Сайт доски объявлений включает в себя следующие страницы:
главная - показывающая десять последних опубликованных объявлений без разбиения их на рубрики;
страница списка объявлений - показывающая (с использованием пагинации) объявления из определенной рубрики. Также она будет содержать форму для поиска объявления по введенному слову;
страница сведений о выбранном объявлении - выведет еще все оставленные для него комментарии и форму для добавления нового комментария;
страницы регистрации и активации нового пользователя;
страницы входа и выхода;
страница профиля зарегистрированного пользователя - выведет список объявлений, оставленных текущим пользователем;
страницы добавления, правки, удаления объявлений;
страницы изменения пароля, правки и удаления пользовательского профиля;
страницы сведений о сайте, о правах его разработчика, пользовательского соглашения и пр.




Superuser:  
> Name:           postgres  
  E-mail address: postgres@postgres.com            
  Password:       postgres

HOW TO RUN:
>python3 manage.py runserver --nostatic
